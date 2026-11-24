from .analyzer import OmekaSAnalyzer

# SDK v2 (AC-403): re-exported module-level declaration, kept in sync with
# the class attribute on OmekaSAnalyzer.
EXTRACTION_PROTOCOL_VERSION = "2.0"

__all__ = ["EXTRACTION_PROTOCOL_VERSION", "OmekaSAnalyzer"]
