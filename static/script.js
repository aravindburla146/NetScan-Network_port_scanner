const scanButton = document.getElementById("scan-button");

scanButton.addEventListener("click", async () => {

    const target = document.getElementById("target").value.trim();
    const startPort = document.getElementById("start-port").value;
    const endPort = document.getElementById("end-port").value;

    // Basic validation
    if (!target || !startPort || !endPort) {
        alert("Please enter target, start port, and end port.");
        return;
    }

    // Disable button during scan
    scanButton.disabled = true;
    scanButton.textContent = "🔄 Scanning...";

    const resultsContainer = document.getElementById("results-container");

    resultsContainer.innerHTML = `
        <p class="scanning-message">
            🔄 Scanning ${target}...
            <br>
            Please wait while NetScan checks the selected ports.
        </p>
    `;

    try {

        const response = await fetch("/scan", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                target: target,
                start_port: startPort,
                end_port: endPort
            })
        });

        const data = await response.json();

        // Handle server errors
        if (!response.ok) {
            resultsContainer.innerHTML = `
                <p class="error-message">
                    ${data.error || "An error occurred during the scan."}
                 </p>
            `;
            return;
        }

        // Update statistics
        document.getElementById("ports-scanned").textContent =
            data.ports_scanned;

        document.getElementById("open-ports").textContent =
            data.open_ports;

        document.getElementById("scan-time").textContent = 
            data.scan_time + " sec";

        // Display results
        displayResults(data.results);

        // Show CSV download button
        const reportContainer = document.getElementById("report-container");

        reportContainer.innerHTML = `
            <a
                href="/download/${data.report}"
                class="download-button"
                download
            >
                📥 Download CSV Report
            </a>
        `;

    } catch (error) {

        console.error(error);

        alert("An error occurred while scanning.");

    } finally {

        // Re-enable button
        scanButton.disabled = false;
        scanButton.textContent = "🚀 Start Scan";
    }
});


function displayResults(results) {

    const container = document.getElementById("results-container");

    // No open ports
    if (results.length === 0) {

        container.innerHTML = `
            <p class="no-results">
                No open ports detected.
            </p>
        `;

        return;
    }

    let table = `
        <table>
            <thead>
                <tr>
                    <th>Port</th>
                    <th>Status</th>
                    <th>Service</th>
                </tr>
            </thead>
            <tbody>
    `;

    results.forEach(result => {

        table += `
            <tr>
                <td>${result.port}</td>
                <td class="open-status">${result.status}</td>
                <td>${result.service}</td>
            </tr>
        `;

    });

    table += `
            </tbody>
        </table>
    `;

    container.innerHTML = table;
}