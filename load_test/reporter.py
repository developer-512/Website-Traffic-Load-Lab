import os
from statistics import mean
from datetime import datetime, timezone
from jinja2 import Template

REPORT_DIR = "artifacts/reports"
CHART_DIR = "artifacts/charts"
SCREENSHOT_DIR = "artifacts/screenshots"

def generate_report(results, cpu, mem, start_time):
    os.makedirs(REPORT_DIR, exist_ok=True)

    times = [r["time"] for r in results]
    errors = [r for r in results if r["error"]]

    total = len(results)
    error_count = len(errors)

    def pct(p):
        if not times:
            return 0
        times_sorted = sorted(times)
        idx = int(len(times_sorted) * p / 100)
        return round(times_sorted[min(idx, len(times_sorted)-1)], 3)

    stats = {
        "total": total,
        "errors": error_count,
        "error_rate": round((error_count / total) * 100, 2) if total else 0,
        "avg": round(mean(times), 3) if times else 0,
        "p50": pct(50),
        "p90": pct(90),
        "p95": pct(95),
        "p99": pct(99),
        "cpu_avg": round(mean(cpu), 2) if cpu else 0,
        "mem_avg": round(mean(mem), 2) if mem else 0,
        "start": start_time.isoformat(),
        "end": datetime.now(timezone.utc).isoformat(),
    }

    template_path = "templates/report.html"

    with open(template_path, encoding="utf-8") as f:
        template = Template(f.read())

    html = template.render(
        stats=stats,
        results=results,
        charts={
            "latency": f"{CHART_DIR}/latency.png"
        },
        screenshots={
            "before": f"{SCREENSHOT_DIR}/before_test.png",
            "after": f"{SCREENSHOT_DIR}/after_test.png"
        }
    )

    report_path = f"{REPORT_DIR}/load_test_report.html"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"HTML report generated: {report_path}")
