import pytest
from scripts.manual_review import evaluate_stock

def packet():
    return {"stock":{"symbol":"TEST","price":10,"prev_close":9,"avg_volume":100,"volume":200},"analyst":{"fundamentals_score":1,"technicals_score":1},"radar":{"sentiment_score":1,"news_momentum":1,"controversy":0},"insider":{"insider_buying":1,"insider_selling":0,"institutional_flow":1,"cluster_buying":True},"pulse":{"go_signal":1},"sources":[{"url":"https://example.com","observed_at":"2026-01-01T00:00:00Z"}]}
def test_manual_review_never_enables_orders():
    result=evaluate_stock(packet()); assert result["decision"]=="REVIEW"; assert result["orders_enabled"] is False
def test_hard_veto_is_preserved():
    data=packet(); data["radar"]["controversy"]=0.9; result=evaluate_stock(data); assert result["decision"]=="REJECT"; assert result["reason"]=="veto_controversy"
def test_sources_are_required():
    data=packet(); data["sources"]=[]
    with pytest.raises(ValueError,match="non-empty"): evaluate_stock(data)
