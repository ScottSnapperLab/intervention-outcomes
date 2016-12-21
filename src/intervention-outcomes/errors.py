#!/usr/bin/env python
"""Provide error classes for intervention-outcomes."""

# Imports


# Metadata
__author__ = "Gus Dunn"
__email__ = "w.gus.dunn@gmail.com"




class Intervention-outcomesError(Exception):

    """Base error class for intervention-outcomes."""


class ValidationError(Intervention-outcomesError):

    """Raise when a validation/sanity check comes back with unexpected value."""
