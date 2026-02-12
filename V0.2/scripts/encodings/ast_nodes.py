#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Abstract Syntax Tree nodes for TECHDOC encoding conversion.

This module defines the core data structures used to represent TECHDOC
documents in a format-agnostic way, enabling conversion between
Markdown, JSON, and XML encodings.
"""

from dataclasses import dataclass
from enum import Enum
from typing import List, Optional


class SectionType(Enum):
    """Enumeration of TECHDOC section types."""
    NARRATIVE = "narrative"
    ASSERTION = "assertion"
    DATA = "data"
    INHERITANCE = "inheritance"


class VerificationIndicator(Enum):
    """Enumeration of verification indicators for normative statements."""
    PROVABLE = "provable"  # Ⓟ
    TESTABLE = "testable"  # Ⓣ
    EVALUATABLE = "evaluatable"  # Ⓔ
    HEURISTIC = "heuristic"  # Ⓗ
    NON_VERIFIABLE = "non_verifiable"  # Ⓝ

    @classmethod
    def from_unicode(cls, char: str) -> Optional["VerificationIndicator"]:
        """Convert unicode verification indicator to enum."""
        mapping = {
            "Ⓟ": cls.PROVABLE,
            "Ⓣ": cls.TESTABLE,
            "Ⓔ": cls.EVALUATABLE,
            "Ⓗ": cls.HEURISTIC,
            "Ⓝ": cls.NON_VERIFIABLE,
        }
        return mapping.get(char)

    def to_unicode(self) -> str:
        """Convert enum to unicode verification indicator."""
        mapping = {
            self.PROVABLE: "Ⓟ",
            self.TESTABLE: "Ⓣ",
            self.EVALUATABLE: "Ⓔ",
            self.HEURISTIC: "Ⓗ",
            self.NON_VERIFIABLE: "Ⓝ",
        }
        return mapping[self]


@dataclass
class Statement:
    """Represents a single statement within a TECHDOC section."""
    content: str
    statement_id: Optional[str] = None
    verification_indicator: Optional[VerificationIndicator] = None


@dataclass
class Section:
    """Represents a TECHDOC section."""
    name: str
    section_type: SectionType
    statements: List[Statement]
    data_language: Optional[str] = None
    data_content: Optional[str] = None
    # Inheritance section specific fields
    conforms_to: Optional[List[str]] = None
    inherits: Optional[List[str]] = None


@dataclass
class Techdoc:
    """Represents a complete TECHDOC document."""
    title: str
    sections: List[Section]

    def get_section_by_name(self, name: str) -> Optional[Section]:
        """Retrieve a section by its name."""
        for section in self.sections:
            if section.name == name:
                return section
        return None

    def add_section(self, section: Section) -> None:
        """Add a section to the document."""
        self.sections.append(section)
