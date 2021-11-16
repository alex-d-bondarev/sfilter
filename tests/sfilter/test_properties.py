from src.sfilter.file_handling.file_finder import find_file
from src.sfilter.setup_handler import SetUpHandler


def test_sfilter_section_is_present():
    assert SetUpHandler().has_section("sfilter")

def test_setup_writes_without_changes():
    content_before = find_file("setup.cfg").get_content()
    SetUpHandler().save()
    content_after = find_file("setup.cfg").get_content()
    assert content_before == content_after
