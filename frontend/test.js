function calculateResult() {

    let growth = 0;
    let value = 0;
    let quality = 0;

    const form = document.getElementById("quizForm");
    const formData = new FormData(form);

    for (let answer of formData.values()) {

        if (answer === "growth") growth++;
        else if (answer === "value") value++;
        else quality++;

    }

    let result = "";
    let reason = "";
    let sectors = "";
    let risk = "";
    let strategy = "";
    let color = "#10b981";

    if (growth >= value && growth >= quality) {

        result = "🚀 Growth Investor";
        strategy = "growth";

        reason =
        "You focus on companies that can grow revenue and profits rapidly. You are willing to tolerate short-term volatility in exchange for potentially higher long-term returns.";

        sectors =
        "Technology, Manufacturing, Capital Goods, Renewable Energy";

        risk =
        "High Risk • High Reward";

        color = "#3b82f6";

    }

    else if (value >= growth && value >= quality) {

        result = "💰 Value Investor";
        strategy = "value";

        reason =
        "You look for companies trading below their intrinsic value. You prefer buying strong businesses at attractive prices and waiting patiently for the market to recognize their worth.";

        sectors =
        "Banking, FMCG, Conglomerates, Energy";

        risk =
        "Moderate Risk • Moderate Reward";

        color = "#f59e0b";

    }

    else {

        result = "🏆 Quality Investor";
        strategy = "quality";

        reason =
        "You prefer businesses with strong management, healthy profitability, low debt, and consistent performance. Stability matters more than chasing aggressive growth.";

        sectors =
        "IT Services, Consumer Brands, Pharma, Insurance";

        risk =
        "Lower Risk • Stable Returns";

        color = "#10b981";

    }

    document.getElementById("result").innerHTML = `

        <div style="
            background:#111827;
            border-radius:20px;
            padding:30px;
            margin-top:30px;
            border:1px solid rgba(255,255,255,.08);
            text-align:left;
        ">

            <h2 style="
                color:${color};
                margin-bottom:15px;
                font-size:32px;
            ">
                ${result}
            </h2>

            <p style="
                line-height:1.8;
                color:#d1d5db;
            ">
                ${reason}
            </p>

            <hr style="
                border:none;
                border-top:1px solid rgba(255,255,255,.08);
                margin:20px 0;
            ">

            <p>
                <strong>📊 Risk Profile:</strong><br>
                ${risk}
            </p>

            <br>

            <p>
                <strong>🏭 Recommended Sectors:</strong><br>
                ${sectors}
            </p>

            <br>

            <p>
                <strong>🎯 Suggested DeltaView Mode:</strong><br>
                ${result}
            </p>

            <br>

            <button
onclick="window.location.href='index.html?strategy=${strategy}'"
style="
    width:100%;
    background:${color};
    color:black;
    border:none;
    padding:14px;
    border-radius:12px;
    font-weight:bold;
    cursor:pointer;
    font-size:16px;
">
    View My Recommended Stocks →
</button>

        </div>
    `;

    
}