let portfolio =
JSON.parse(localStorage.getItem("portfolio")) || [];

let allocationChart = null;

function savePortfolio() {

    localStorage.setItem(
        "portfolio",
        JSON.stringify(portfolio)
    );

}

function clearPortfolio() {

    if(confirm("Delete entire portfolio?")) {

        portfolio = [];

        savePortfolio();

        renderPortfolio();
    }
}

function deleteStock(index) {

    portfolio.splice(index, 1);

    savePortfolio();

    renderPortfolio();
}

function addStock() {

    const company =
        document.getElementById("stockName").value.trim();

    const quantity =
        Number(document.getElementById("quantity").value);

    const buyPrice =
        Number(document.getElementById("buyPrice").value);

    if(!company || !quantity || !buyPrice) {

        alert("Fill all fields");

        return;
    }

    portfolio.push({

        company,
        quantity,
        buyPrice

    });

    savePortfolio();

    renderPortfolio();

    document.getElementById("stockName").value = "";
    document.getElementById("quantity").value = "";
    document.getElementById("buyPrice").value = "";
}

function renderPortfolio() {

    const tbody =
        document.querySelector(
            "#portfolioTable tbody"
        );

    tbody.innerHTML = "";

    let invested = 0;

    portfolio.forEach((stock,index) => {

        const value =
            stock.quantity *
            stock.buyPrice;

        invested += value;

        tbody.innerHTML += `
        <tr>

            <td>${stock.company}</td>

            <td>${stock.quantity}</td>

            <td>₹${stock.buyPrice}</td>

            <td>₹${value.toLocaleString()}</td>

            <td>
                <button
                class="delete-btn"
                onclick="deleteStock(${index})">
                🗑 Delete
                </button>
            </td>

        </tr>
        `;
    });

    document.getElementById(
        "holdingCount"
    ).innerText =
    portfolio.length;

    document.getElementById(
        "totalInvested"
    ).innerText =
    "₹" + invested.toLocaleString();

    let score =
        Math.min(
            50 + portfolio.length * 10,
            100
        );

    document.getElementById(
        "healthScore"
    ).innerText =
    score + "/100";

    let insight =
    "Portfolio needs diversification.";

    if(portfolio.length >= 3) {

        insight =
        "Good diversification across multiple holdings.";
    }

    if(portfolio.length >= 5) {

        insight =
        "Well diversified portfolio with balanced exposure.";
    }

    if(portfolio.length >= 10) {

        insight =
        "Excellent diversification and lower concentration risk.";
    }

    document.getElementById(
        "portfolioInsight"
    ).innerText =
    insight;

    renderAllocationChart();
}

function renderAllocationChart() {

    const canvas =
    document.getElementById(
        "allocationChart"
    );

    if(!canvas) return;

    const labels =
    portfolio.map(
        stock => stock.company
    );

    const values =
    portfolio.map(
        stock =>
        stock.quantity *
        stock.buyPrice
    );

    if(allocationChart) {
        allocationChart.destroy();
    }

    if(values.length === 0) {
        return;
    }

    allocationChart =
    new Chart(canvas, {

        type: "doughnut",

        data: {

            labels: labels,

            datasets: [{

                data: values,

                backgroundColor: [

                    "#00ff99",
                    "#00c2ff",
                    "#ffd93d",
                    "#ff6b6b",
                    "#a855f7",
                    "#14b8a6",
                    "#f97316",
                    "#22c55e",
                    "#ec4899",
                    "#3b82f6"

                ],

                borderWidth: 0

            }]

        },

        options: {

            responsive: true,

            maintainAspectRatio: false,

            plugins: {

                legend: {

                    position: "bottom",

                    labels: {

                        color: "white"

                    }

                }

            }

        }

    });
}

renderPortfolio();