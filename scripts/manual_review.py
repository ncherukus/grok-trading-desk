#!/usr/bin/env python3
"""Deterministic manual-Codex review. This module contains no execution path."""
from __future__ import annotations
import argparse, json
from pathlib import Path
import sys
from typing import Any

sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from src.models import Stock
from src.stocks.stock_scoring import score_stock

REQUIRED_BLOCKS=("stock","analyst","radar","insider","pulse","sources")
def evaluate_stock(packet:dict[str,Any])->dict[str,Any]:
    missing=[key for key in REQUIRED_BLOCKS if key not in packet]
    if missing: raise ValueError("missing blocks: "+", ".join(missing))
    if not isinstance(packet["sources"],list) or not packet["sources"]: raise ValueError("sources must be a non-empty list")
    for source in packet["sources"]:
        if not isinstance(source,dict) or not source.get("url") or not source.get("observed_at"): raise ValueError("each source needs url and observed_at")
    stock=Stock.model_validate(packet["stock"]); verdict=score_stock(stock,packet["analyst"],packet["radar"],packet["insider"],packet["pulse"])
    return {"mode":"manual_codex_paper_only","symbol":stock.symbol,"decision":"REVIEW" if verdict["buy"] else "REJECT","score":verdict["score"],"reason":verdict["reason"],"vetoed":verdict["vetoed"],"components":verdict["components"],"sources":packet["sources"],"orders_enabled":False}
def main()->int:
    parser=argparse.ArgumentParser(description="Score a Codex research packet without execution"); parser.add_argument("market",choices=["stock"]); parser.add_argument("--input",required=True,type=Path); parser.add_argument("--output",type=Path); args=parser.parse_args()
    result=evaluate_stock(json.loads(args.input.read_text(encoding="utf-8"))); rendered=json.dumps(result,indent=2)
    if args.output: args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(rendered+"\n",encoding="utf-8")
    print(rendered); return 0
if __name__=="__main__": raise SystemExit(main())
