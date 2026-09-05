# Stock review packet

Required blocks are `stock`, `analyst`, `radar`, `insider`, `pulse`, and `sources`.

- `stock`: fields accepted by `src.models.Stock`, including symbol, price, previous close, current volume, and average volume.
- `analyst`: `fundamentals_score`, `technicals_score`, and `summary`. Missing scores default to zero.
- `radar`: `sentiment_score`, `news_momentum`, `controversy`, and `summary`. Missing controversy defaults to one and vetoes the candidate.
- `insider`: `insider_buying`, `insider_selling`, `institutional_flow`, `cluster_buying`, and `summary`. Missing values default to no buying and maximum selling.
- `pulse`: `go_signal`, `risk_appetite`, `regime`, and `notes`. Missing go signal defaults to zero and vetoes the candidate.
- `sources`: a non-empty list of objects with `url`, `observed_at`, and optional `note`.

All score fields range from zero to one. Use current filings and issuer or exchange data for factual claims, and distinguish facts from judgment.
