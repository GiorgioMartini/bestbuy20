import pytest
from products import Product

@pytest.fixture
def sample_product():
    """Fixture that returns a basic product instance for testing"""
    return Product(
        name="Test Product",
        price=9.99,
        quantity=10
    )

def test_product_creation(sample_product):
    """Test that a product is created with correct attributes"""
    assert sample_product.name == "Test Product"
    assert sample_product.price == 9.99
    assert sample_product.quantity == 10

def test_product_price_validation():
    """Test that product price cannot be negative"""
    with pytest.raises(ValueError):
        Product(name="Invalid Product", price=-10.00, quantity=5)

def test_product_name_validation():
    """Test that product price cannot be negative"""
    with pytest.raises(ValueError):
        Product(name='', price=-10.00, quantity=5)

def test_product_quantity_validation():
    """Test that product quantity cannot be negative"""
    with pytest.raises(ValueError):
        Product(name="Invalid Product", price=10.00, quantity=-5)

def test_product_buying_quantity_validation():
    """Test that product buying quantity cannot be greater than the quantity in stock"""
    with pytest.raises(ValueError):
        p = Product(name="Invalid Product", price=10.00, quantity=5)
        p.buy(10)

def test_product_returns_correct_stock_after_buy():
    """Test that product returns correct stock after buy"""
    p = Product(name="Invalid Product", price=10.00, quantity=10)
    res = p.buy(5)
    assert res == 50

def test_product_turns_negative_after_outta_stock():
    """Test that product returns correct stock after buy"""
    p = Product(name="Invalid Product", price=10.00, quantity=10)
    res = p.buy(10)
    assert p.is_active() == False
