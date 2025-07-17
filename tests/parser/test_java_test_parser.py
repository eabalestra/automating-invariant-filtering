import pytest

from src.parser.java_test_parser import JavaTestParser


@pytest.fixture
def parser():
    return JavaTestParser()


def test_parse_simple_test_method(parser):
    """Test parsing a simple Java test method with comments."""
    input_string = """
    // This is a comment before the test
    // Another comment line
    @Test
    public void testExample() {
        assertEquals(1, 1);
    }
    // This is a comment after the test
    // Another comment line
    """

    comments, test_methods = parser.parse(input_string)

    # Should have exactly one test method
    assert len(test_methods) == 1

    # The test method should contain the @Test annotation and method body
    test_method = test_methods[0]
    assert "@Test" in test_method
    assert "public void testExample()" in test_method
    assert "assertEquals(1, 1);" in test_method

    # Comments should contain the lines that are not part of the test
    assert len(comments) > 0
    assert any(
        "// This is a comment before the test" in comment for comment in comments)
