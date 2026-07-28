const printButton = document.querySelector("[data-print-sourcebook]");

if (printButton) {
  printButton.addEventListener("click", () => window.print());
}

// Maintainers can append ?folio=7 to render one page at a time during visual
// review. Normal readers and the PDF build always see the complete dossier.
const requestedFolio = new URLSearchParams(window.location.search).get("folio");

if (requestedFolio) {
  const selectedFolio = document.querySelector(
    `[data-folio="${CSS.escape(requestedFolio)}"]`,
  );

  if (selectedFolio) {
    document.body.classList.add("single-folio-preview");

    for (const folio of document.querySelectorAll("[data-folio]")) {
      folio.hidden = folio !== selectedFolio;
    }
  }
}
