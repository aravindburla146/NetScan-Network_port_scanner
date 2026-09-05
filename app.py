from flask import Flask, render_template, request, jsonify, send_from_directory
from scanner import validate_target, scan_target
import csv
import os
from datetime import datetime

app = Flask(__name__)
REPORT_FOLDER = "reports"

os.makedirs(REPORT_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/scan", methods=["POST"])
def scan():
    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "error": "Invalid request data."
        }), 400

    target = data.get("target", "").strip()
    start_port = data.get("start_port")
    end_port = data.get("end_port")

    # Validate target
    if not validate_target(target):
        return jsonify({
            "error": "Invalid IP address or hostname."
        }), 400

    # Validate ports
    try:
        start_port = int(start_port)
        end_port = int(end_port)
    except (ValueError, TypeError):
        return jsonify({
            "error": "Ports must be valid numbers."
        }), 400

    if not (1 <= start_port <= 65535):
        return jsonify({
            "error": "Start port must be between 1 and 65535."
        }), 400

    if not (1 <= end_port <= 65535):
        return jsonify({
            "error": "End port must be between 1 and 65535."
        }), 400

    if start_port > end_port:
        return jsonify({
            "error": "Start port cannot be greater than end port."
        }), 400

    # Create port list
    ports = list(range(start_port, end_port + 1))

    # Run scanner
    scan_data = scan_target(target, ports)
    results = scan_data["results"]
    duration = scan_data["duration"]

    # Generate CSV report
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"netscan_report_{timestamp}.csv"
    filepath = os.path.join(REPORT_FOLDER, filename)

    with open(filepath, "w", newline="", encoding="utf-8") as csvfile:

        writer = csv.writer(csvfile)

        writer.writerow([
            "Target",
            "Port",
            "Status",
            "Service"
        ])

        for result in results:

            writer.writerow([
                target,
                result["port"],
                result["status"],
                result["service"]
            ])

    # Calculate statistics
    open_ports = [
        result for result in results
        if result["status"] == "Open"
    ]

    return jsonify({
    "target": target,
    "ports_scanned": len(results),
    "open_ports": len(open_ports),
    "scan_time": duration,
    "results": open_ports,
    "report": filename
})

@app.route("/download/<filename>")
def download_report(filename):
    return send_from_directory(
        REPORT_FOLDER,
        filename,
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)