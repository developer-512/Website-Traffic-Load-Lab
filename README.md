# Website Traffic Load Lab

Advanced diagnostic load testing toolkit for PHP / MySQL applications.

## Features
- Concurrent async load testing
- Weighted multi-endpoint traffic
- Timeout & error classification
- CPU & memory sampling
- MySQL slow query correlation
- Latency charts
- Automatic Chrome screenshots
- Rich HTML reports

## Install
```bash
pip install -r requirements.txt
playwright install chromium
```

```bash
cp config/endpoints.example.json config/endpoints.json
cp config/mysql.example.json config/mysql.json
cp config/thresholds.example.json config/thresholds.json
```
Add you website endpoints into config/endpoints.json

```json

[
  {
    "url": "https://example.com/",
    "weight": 100
  }
]

```

## Run
```bash
python run.py --clients 25 --duration 60 --timeout 5
```

Report will be generated in:

artifacts/reports/load_test_report.html



