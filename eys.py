#!/usr/bin/env python3
from dataclasses import dataclass


# https://docs.google.com/document/d/1w1glX3H05ZpXkijFLtNr0kI7_tyzkAQo50x5iaSW-Tg

@dataclass(frozen=True, order=True)
class Duration:
    seconds: int

    def minutes(self) -> float:
        return self.seconds / 60

    def hours(self) -> float:
        return self.minutes() / 60

    @staticmethod
    def from_minutes(minutes: float) -> "Duration":
        return Duration(int(minutes * 60))

    @staticmethod
    def from_hours(hours: float) -> "Duration":
        return Duration.from_minutes(hours * 60)

    def __mul__(self, other: float) -> "Duration":
        return Duration(int(self.seconds * other))


def async_to_sync_time(duration: Duration) -> Duration:
    if duration < Duration.from_minutes(5):
        return duration
    if duration < Duration.from_minutes(15):
        return duration * 0.5
    if duration < Duration.from_hours(1):
        return duration * 0.25
    if duration < Duration.from_hours(8):
        return duration * 0.1
    return duration * 0.05


if __name__ == "__main__":
    print("Hello, World!")
