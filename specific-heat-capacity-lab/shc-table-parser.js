// Website: https://www.engineeringtoolbox.com/specific-heat-solids-d_154.html
// Set the desired value and the uncertainty in kJ/(kg K)
const desired_value = 0.60;
const uncertainty = 0.10;
// Extract the table element
const table = document.querySelector("table.medium.tablesorter");
const table_body = table.querySelector("tbody");
// Delete rows that do not fall within the uncertainty range
for (let i = table_body.children.length - 1; i >= 0; i--) {
  const row = table_body.children[i];
  const value = parseFloat(row.children[2].textContent);
  const within_uncertainty = Math.abs(value - desired_value) <= uncertainty;
  if (!within_uncertainty) {
    table_body.removeChild(row);
  }
}
