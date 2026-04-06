from app import app


# Test 1 -header
def test_header_is_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("h1", timeout=10)

# Test 2 - visualisation
def test_visualization_is_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#sales-line-chart", timeout=10)

# Test 3 - region picker
def test_region_picker_is_present(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region-filter", timeout=10)