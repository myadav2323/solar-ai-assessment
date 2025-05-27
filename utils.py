def estimate_roi(annual_generation_kwh, panel_count):
    cost_per_panel = 25000  # ₹ per panel
    price_per_kwh = 8       # ₹/unit

    total_cost = panel_count * cost_per_panel
    annual_savings = annual_generation_kwh * price_per_kwh
    payback_years = round(total_cost / annual_savings, 1) if annual_savings else float("inf")

    return {
        "cost": total_cost,
        "savings": annual_savings,
        "payback_years": payback_years
    }
