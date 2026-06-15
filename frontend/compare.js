async function runComparison() {

    const c1 = document.getElementById("company1").value;
    const c2 = document.getElementById("company2").value;

    const res = await fetch(
        `http://127.0.0.1:8000/compare?company1=${c1}&company2=${c2}`
    );

    const data = await res.json();
    const m = data.metrics;

    function metricCard(name, v1, v2, reverse=false) {

        let better1 = reverse ? v1 < v2 : v1 > v2;
        let better2 = !better1;

        let max = Math.max(v1, v2, 1);

        return `
        <div class="card">
            <h3>${name}</h3>

            <div class="values">
                <div class="val ${better1 ? 'green' : 'red'}">
                    ${v1}
                    <div class="bar" style="width:${(v1/max)*100}%"></div>
                </div>

                <div class="val ${better2 ? 'green' : 'red'}">
                    ${v2}
                    <div class="bar" style="width:${(v2/max)*100}%"></div>
                </div>
            </div>
        </div>`;
    }

    // Metrics UI
    document.getElementById("output").innerHTML = `
        <div class="header">
            <h2>${data.company1}</h2>
            <h2>${data.company2}</h2>
        </div>

        ${metricCard("Sales Growth", m.sales_cagr[0], m.sales_cagr[1])}
        ${metricCard("Profit Growth", m.profit_cagr[0], m.profit_cagr[1])}
        ${metricCard("Operating Margin", m.avg_operating_margin[0], m.avg_operating_margin[1])}
        ${metricCard("Debt (Lower Better)", m.debt_to_cashflow[0], m.debt_to_cashflow[1], true)}
    `;

    // Score logic
    let score1 = 0;
    let score2 = 0;

    function score(v1, v2, reverse=false) {
        if (reverse) {
            v1 < v2 ? score1++ : score2++;
        } else {
            v1 > v2 ? score1++ : score2++;
        }
    }

    score(m.sales_cagr[0], m.sales_cagr[1]);
    score(m.profit_cagr[0], m.profit_cagr[1]);
    score(m.avg_operating_margin[0], m.avg_operating_margin[1]);
    score(m.debt_to_cashflow[0], m.debt_to_cashflow[1], true);

    document.getElementById("verdict").innerHTML =
        score1 > score2
        ? `🏆 ${data.company1} Wins`
        : `🏆 ${data.company2} Wins`;

    // Fetch charts
    const d1 = await fetch(`http://127.0.0.1:8000/company?company=${c1}`).then(r => r.json());
    const d2 = await fetch(`http://127.0.0.1:8000/company?company=${c2}`).then(r => r.json());

    new Chart(document.getElementById("revChart"), {
        type: "line",
        data: {
            labels: d1.years,
            datasets: [
                { label: data.company1, data: d1.revenue, borderColor: "green" },
                { label: data.company2, data: d2.revenue, borderColor: "red" }
            ]
        }
    });

    new Chart(document.getElementById("profitChart"), {
        type: "line",
        data: {
            labels: d1.years,
            datasets: [
                { label: data.company1, data: d1.profit, borderColor: "green" },
                { label: data.company2, data: d2.profit, borderColor: "red" }
            ]
        }
    });
}