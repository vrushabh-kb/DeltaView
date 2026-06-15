async function loadCompanies(strategy = "quality") {

    const container = document.getElementById("companyList");

    container.innerHTML = "Loading companies...";

    try {

        const response = await fetch(
            `http://127.0.0.1:8000/rank?strategy=${strategy}`
        );

        const data = await response.json();

        container.innerHTML = "";

        data.forEach(company => {

            const card = document.createElement("div");

            card.className = "company-card";

            const reasons =
                company.reason && company.reason.length > 0
                ? company.reason.map(r =>
                    `<div class="reason-item">✅ ${r}</div>`
                  ).join("")
                : `<div class="reason-item">📊 Balanced Fundamentals</div>`;

            card.innerHTML = `

                <div class="company-header">

                    <h3>${company.company}</h3>

                    <span class="rank-badge">
                        #${company.rank}
                    </span>

                </div>

                <div class="score-section">

                    <div class="score-circle">
                        ${Math.round(company.score)}
                    </div>

                    <div>

                        <p class="score-label">
                            DeltaScore™
                        </p>

                        <div class="mini-bar">

                            <div
                                class="mini-fill"
                                style="width:${company.score}%">
                            </div>

                        </div>

                    </div>

                </div>

                <div class="reason-box">

                    <strong>
                        Why Ranked?
                    </strong>

                    ${reasons}

                </div>

                <button class="analyze-btn">
                    Analyze →
                </button>

            `;

            card.onclick = () => {

                window.location.href =
                    `company.html?name=${company.company}`;

            };

            container.appendChild(card);

        });

    }

    catch (error) {

        console.error(error);

        container.innerHTML =
            "Error loading companies";

    }

}


// --------------------------------------------------
// SEARCH
// --------------------------------------------------

document.getElementById("searchInput")
.addEventListener("input", function () {

    const search =
        this.value.toLowerCase();

    const cards =
        document.querySelectorAll(".company-card");

    cards.forEach(card => {

        const name =
            card.querySelector("h3")
            .innerText
            .toLowerCase();

        if (name.includes(search)) {

            card.style.display = "block";

        }

        else {

            card.style.display = "none";

        }

    });

});


// --------------------------------------------------
// INITIAL LOAD
// --------------------------------------------------

const params =
    new URLSearchParams(window.location.search);

const strategyFromURL =
    params.get("strategy");

if (strategyFromURL) {

    loadCompanies(strategyFromURL);

}

else {

    loadCompanies();

}