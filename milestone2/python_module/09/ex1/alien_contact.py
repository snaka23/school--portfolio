from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from enum import Enum


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
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def check_AlienContact(self) -> "AlienContact":
        if not (self.contact_id[0] == "A" and self.contact_id[1] == "C"):
            raise ValueError("contact_id doesn't start 'AC'")
        if self.contact_type == ContactType.PHYSICAL:
            if not self.is_verified:
                raise ValueError(
                    "if contact_type is physical, "
                    "is_verified should True"
                )
        if self.contact_type == ContactType.TELEPATHIC:
            if self.witness_count < 3:
                raise ValueError(
                    "if contact_type is telepathic, "
                    "witness_count should be more than 2"
                )
        if self.signal_strength > 7.0:
            if not self.message_received:
                raise ValueError(
                    "if signal_strength is more than 7.0, "
                    "message_received should be rececived"
                )
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")
    print("Valid contact report:")
    validate_AC = AlienContact(
        contact_id="AC_2024_001",
        timestamp=datetime(2024, 1, 15, 10, 30, 00),
        location="Area 51, Nevada",
        contact_type=ContactType.RADIO,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli"
    )
    print(f"ID: {validate_AC.contact_id}")
    print(f"Type: {validate_AC.contact_type}")
    print(f"Location: {validate_AC.location}")
    print(f"Signal: {validate_AC.signal_strength}/10")
    print(f"Duration: {validate_AC.duration_minutes} minutes")
    print(f"Witness: {validate_AC.witness_count}")
    print(f"Message: '{validate_AC.message_received}'")
    print("\n======================================")
    print("Expected validation error:")
    try:
        AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2024, 1, 15, 10, 30, 0),
            location="Area 51, Nevada",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=1,
            message_received="Greetings from Zeta Reticuli"
        )
    except ValidationError as e:
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
