// Optional client-side logic (e.g. form validation, date picker tweaks)

// Auto-fill today's date in the date field on the new job form
window.addEventListener('DOMContentLoaded', () => {
    const dateInput = document.querySelector('input[name="date"]');
    if (dateInput && !dateInput.value) {
        const today = new Date().toISOString().split('T')[0];
        dateInput.value = today;
    }
});

// Basic client-side form validation
const jobForm = document.querySelector('form');
if (jobForm) {
    jobForm.addEventListener('submit', (e) => {
        const summary = document.querySelector('textarea[name="repair_summary"]');
        if (summary.value.length < 10) {
            alert("Please provide a more detailed repair summary.");
            e.preventDefault();
        }
    });
}
