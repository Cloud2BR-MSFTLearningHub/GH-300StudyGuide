const initializeChecklists = () => {
  const checkboxes = document.querySelectorAll(
    ".md-content .task-list-item input[type='checkbox']",
  );

  checkboxes.forEach((checkbox, index) => {
    if (checkbox.dataset.interactiveChecklist === "true") return;

    const item = checkbox.closest(".task-list-item");
    const label = item?.textContent.trim() || `item-${index}`;
    const storageKey = `gh300-checklist:${location.pathname}:${label}`;

    checkbox.disabled = false;
    checkbox.checked = localStorage.getItem(storageKey) === "true";
    checkbox.dataset.interactiveChecklist = "true";
    checkbox.setAttribute("aria-label", label);
    checkbox.addEventListener("change", () => {
      localStorage.setItem(storageKey, String(checkbox.checked));
    });
  });
};

document.addEventListener("DOMContentLoaded", initializeChecklists);

if (typeof document$ !== "undefined") {
  document$.subscribe(initializeChecklists);
}