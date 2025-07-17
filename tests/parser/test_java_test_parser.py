import pytest
from textwrap import dedent

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


def test_parse_simple_test_method_with_comments(parser):
    input_string = dedent("""
        This is a comment before the test
        @Test
        public void testExample() {
            assertEquals(1, 1);
        }
        This is a comment after the test
    """).strip()

    expected_result = dedent("""
        // This is a comment before the test
        // This is a comment after the test
        @Test
        public void testExample() {
            assertEquals(1, 1);
        }
    """).strip()

    result = parser.parse_test_with_comments(input_string)

    assert result == expected_result


def test_parse_multiple_test_method_with_multiple_comments(parser):
    input_string = dedent("""
        This is a comment before the test
        @Test
        public void testExample() {
            // This is a comment inside the test
            assertEquals(1, 1);
        }
        This is a comment after the test
        @Test
        public void testExample() {
            assertEquals(1, 1);
        } [[This is a comment after the test]] 
        This is a comment after the test
    """).strip()

    expected_result = dedent("""
        // This is a comment before the test
        // This is a comment after the test
        // [[This is a comment after the test]]
        // This is a comment after the test
        @Test
        public void testExample() {
            // This is a comment inside the test
            assertEquals(1, 1);
        }
        @Test
        public void testExample() {
            assertEquals(1, 1);
        }
    """).strip()

    result = parser.parse_test_with_comments(input_string)

    assert result == expected_result
