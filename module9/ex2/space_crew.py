from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from typing import List
from enum import Enum


class Rank(str, Enum):
    """Patentes da tripulação."""
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission_safety(self) -> 'SpaceMission':

        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')

        leader_count = 0
        for member in self.crew:
            if member.rank == Rank.COMMANDER or member.rank == Rank.CAPTAIN:
                leader_count += 1

        if leader_count == 0:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        if self.duration_days > 365:
            experienced_count = 0
            for member in self.crew:
                if member.years_experience >= 5:
                    experienced_count += 1

            if experienced_count < len(self.crew) / 2:
                raise ValueError(
                    "Long missions need 50% experienced crew (5+ years)"
                )

        for member in self.crew:
            if member.is_active is False:
                raise ValueError("All crew members must be active")

        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 40)

    try:
        crew_list = [
            CrewMember(
                member_id="CMD01", name="Sarah Connor", rank=Rank.COMMANDER,
                age=45, specialization="Mission Command", years_experience=20
            ),
            CrewMember(
                member_id="LT01", name="John Smith", rank=Rank.LIEUTENANT,
                age=30, specialization="Navigation", years_experience=7
            ),
            CrewMember(
                member_id="OFF01", name="Alice Johnson", rank=Rank.OFFICER,
                age=25, specialization="Engineering", years_experience=3
            )
        ]

        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2024-10-10T08:00:00",
            duration_days=900,
            crew=crew_list,
            budget_millions=2500.0
        )

        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for m in mission.crew:
            print(f"- {m.name} ({m.rank.value}) - {m.specialization}")

    except ValidationError as error_message:
        print(f"Unexpected error: {error_message}")

    print("=" * 40)

    print("Expected validation error:")
    try:
        SpaceMission(
            mission_id="M_FAIL",
            mission_name="Unauthorized Flight",
            destination="Moon",
            launch_date=datetime.now(),
            duration_days=10,
            crew=[
                CrewMember(
                    member_id="CAD01", name="Newbie", rank=Rank.CADET,
                    age=19, specialization="Cleaning", years_experience=0
                )
            ],
            budget_millions=10.0
        )
    except ValidationError as error_message:
        print(error_message.errors()[0]['msg'])


if __name__ == "__main__":
    main()
