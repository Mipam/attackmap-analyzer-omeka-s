"""SDK v2 (AC-403): the analyzer explicitly declares extraction protocol 2.0.

Compat note: v1 payloads still load — ``attackmap.extraction.adapters``
lifts a protocol-1.0 ``ScanResult`` into the v2 ``ExtractionResult``
container, so plugins written against protocol 1.0 keep working
indefinitely via the core adapter.
"""

from attackmap.sdk.analyzer_contracts import declared_extraction_protocol

from attackmap_analyzer_omeka_s import (
    EXTRACTION_PROTOCOL_VERSION,
    OmekaSAnalyzer,
)


def test_analyzer_declares_extraction_protocol_2_0() -> None:
    analyzer = OmekaSAnalyzer()
    assert analyzer.EXTRACTION_PROTOCOL_VERSION == "2.0"
    assert declared_extraction_protocol(analyzer) == "2.0"


def test_module_reexport_matches_class_declaration() -> None:
    assert EXTRACTION_PROTOCOL_VERSION == "2.0"
