#let template(
  title: none,
  authors: (),
  date: datetime.today(),
  college: none,
  course: none,
  crn: none,
  citations: none,
  doc,
) = {
  // Document meta data
  set document(title: title)
  // Page size
  set page("us-letter")
  // Font
  set text(font: "New Computer Modern")
  show raw: set text(font: "New Computer Modern Mono")
  // Paragraphs
  set par(leading: 0.55em, first-line-indent: 1.8em, justify: true)
  show par: set block(spacing: 0.55em)
  // Headings
  set heading(numbering: "1.")
  show heading: set block(above: 1.4em, below: 1em)
  // Math equations
  set math.equation(numbering: "(1)", supplement: [Equation])
  // Header
  set page(header: locate(loc => {
    if counter(page).at(loc).first() > 1 {
      emph(title)
      h(1fr)
      counter(page).display("1")
    }
  }))
  // Tables
  show figure.where(
    kind: table
  ): set figure.caption(position: top)
  set table(stroke: (x, y) => (
    top: if y == 0 { 1pt } else if y == 1 { none } else { 0pt },
    bottom: if y > 0 { 1pt } else { 0.5pt + gray },
  ))
  // Citations
  show bibliography: set heading(numbering: "1.")
  set bibliography(title: [Citations], full: true, style: "ieee")

  // Preface the CRN number with "CRN "
  if crn != none {
    crn = [CRN #crn]
  }
  // Title page
  v(2.5cm)
  text(17pt)[*#title*]
  block(inset: (left: 2cm))[
    *#authors.join(", ")* \ \
    #(college, course, crn).filter(x => {x != none}).join(", ") \
    #date.display("[month repr:long] [day padding:none], [year]") \
  ]
  pagebreak()

  // Main document content
  doc

  // Citations
  if (citations != none) {
    bibliography(citations)
  }
}
