from pydantic import BaseModel, model_validator, ValidationError, Field
from enum import Enum
from datetime import datetime


class Rank(str, Enum):
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
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def check_SpaceMission(self) -> "SpaceMission":
        if self.mission_id[0] != "M":
            raise ValueError("mission_id should start 'M'")
        has_commander_or_captain = False
        experienced = 0
        is_all_active = True
        for member in self.crew:
            if member.rank in (Rank.COMMANDER, Rank.CAPTAIN):
                has_commander_or_captain = True
            if member.years_experience >= 5:
                experienced += 1
            if not member.is_active:
                is_all_active = False
        if not has_commander_or_captain:
            raise ValueError("crew must have Captain or Commander")
        if self.duration_days > 365:
            if experienced / len(self.crew) < 0.5:
                raise ValueError(
                    "Crew must have members "
                    "who were exprienced more than 5years "
                    "more than half of all members"
                )
        if not is_all_active:
            raise ValueError("All member must be active")
        return self


def set_crew_member(
        id: str,
        nm: str,
        rk: Rank,
        ag: int,
        special: str,
        experience: int,
        active: bool = True
) -> "CrewMember":
    return CrewMember(
        member_id=id,
        name=nm,
        rank=rk,
        age=ag,
        specialization=special,
        years_experience=experience,
        is_active=active
    )


def main() -> None:
    print("Space Mission Crew Validation")
    print("======================================")
    crew_member: list[CrewMember] = []
    crew_member.append(
        set_crew_member(
            "12345",
            "Sarah Connor",
            Rank.COMMANDER,
            23,
            "Mission Command",
            5
        )
    )
    crew_member.append(
        set_crew_member(
            "23456",
            "John Smith",
            Rank.LIEUTENANT,
            23,
            "Navigation",
            5
        )
    )
    crew_member.append(
        set_crew_member(
            "34567",
            "Alice Johnson",
            Rank.OFFICER,
            23,
            "Engineering",
            5
        )
    )
    validate_SM = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        duration_days=900,
        budget_millions=2500.0,
        crew=crew_member,
        launch_date=datetime(2026, 8, 25, 17, 00, 00)
    )
    print("Valid mission created:")
    print(f"Mission: {validate_SM.mission_name}")
    print(f"ID: {validate_SM.mission_id}")
    print(f"Destination: {validate_SM.destination}")
    print(f"Duration: {validate_SM.duration_days} days")
    print(f"Budget: ${validate_SM.budget_millions}M")
    print(f"Crew size: {len(validate_SM.crew)}")
    print("Crew members:")
    for member in validate_SM.crew:
        print(f"- {member.name} ({member.rank}) - {member.specialization}")
    print("\n======================================")
    print("Expected validation error:")
    try:
        invalid_crew: list[CrewMember] = []
        invalid_crew.append(
            set_crew_member(
                "12345",
                "Sarah Connor",
                Rank.LIEUTENANT,
                23,
                "Mission Command",
                5
            )
        )
        validate_SM = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            duration_days=900,
            budget_millions=2500.0,
            crew=invalid_crew,
            launch_date=datetime(2026, 8, 25, 17, 00, 00)
        )
    except ValidationError as e:
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
