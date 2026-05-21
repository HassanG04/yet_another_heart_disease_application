document.addEventListener("DOMContentLoaded", function () {
    function syncThemeUi(theme) {
        const icon = document.getElementById("theme-toggle-icon");
        const btn = document.getElementById("theme-toggle");
        if (icon) {
            // Dark mode: offer sun to switch to light. Light mode: offer moon to switch to dark.
            icon.textContent = theme === "dark" ? "☀️" : "🌙";
        }
        if (btn) {
            btn.setAttribute(
                "aria-label",
                theme === "dark" ? "Switch to light theme" : "Switch to dark theme"
            );
        }
    }

    const currentTheme = localStorage.getItem("theme") || "dark";
    document.documentElement.setAttribute("data-bs-theme", currentTheme);
    syncThemeUi(currentTheme);

    const themeToggleBtn = document.getElementById("theme-toggle");
    if (themeToggleBtn) {
        themeToggleBtn.addEventListener("click", function (e) {
            e.preventDefault();
            const current = document.documentElement.getAttribute("data-bs-theme");
            const targetTheme = current === "dark" ? "light" : "dark";
            document.documentElement.classList.add("theme-switching");
            document.documentElement.setAttribute("data-bs-theme", targetTheme);
            localStorage.setItem("theme", targetTheme);
            syncThemeUi(targetTheme);
            window.setTimeout(function () {
                document.documentElement.classList.remove("theme-switching");
            }, 340);
        });
    }

    document.querySelectorAll('[data-bs-toggle="tooltip"]').forEach(function (el) {
        new bootstrap.Tooltip(el);
    });

    document.querySelectorAll(".form-control").forEach(function (input) {
        input.addEventListener("input", function () {
            if (this.value !== "") {
                this.style.borderColor = "#0d6efd";
            } else {
                this.style.borderColor = "";
            }
        });
    });
});
