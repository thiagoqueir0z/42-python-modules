from datetime import datetime
from typing import Optional
from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def validate_business_rules(self) -> 'AlienContact':

        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC"')

        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        if (self.contact_type == ContactType.TELEPATHIC and
                self.witness_count < 3):
            raise ValueError(
                "Telephatic contact requires at least 3 witnesses"
            )

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals (> 7.0) must include a message")

        return self


def main() -> None:
    """Demonstra a validação de relatórios de contacto."""
    print("Alien Contact Log Validation")
    print("=" * 40)

    try:
        report = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli"
        )
        print("Valid contact report:")
        print(f"ID: {report.contact_id}")
        print(f"Type: {report.contact_type.value}")
        print(f"Location: {report.location}")
        print(f"Signal: {report.signal_strength}/10")
        print(f"Duration: {report.duration_minutes} minutes")
        print(f"Witnesses: {report.witness_count}")
        print(f"Message: '{report.message_received}'")

    except ValidationError as error_message:
        print(f"Unexpected error: {error_message}")

    print("=" * 40)

    print("Expected validation error:")
    try:
        AlienContact(
            contact_id="AC_TELE_99",
            timestamp=datetime.now(),
            location="Moon Base Alpha",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=5.0,
            duration_minutes=10,
            witness_count=1
        )
    except ValidationError as error_message:
        print(error_message.errors()[0]['msg'])


if __name__ == "__main__":
    main()
