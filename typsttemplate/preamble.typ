#import "@preview/fletcher:0.5.8" as fletcher: diagram, node, edge
#import "@preview/chic-hdr:0.5.0": *
#import "@preview/ctheorems:1.1.3": *

// #show: thmrules

#let preamble(body) = {
set page(
  header: align(left)[
  ],
  margin: (
    top: 2cm,
    y: 2cm,
  ),
  numbering: "1 of 1",
)

// Configure paragraph properties (indented paras)
set par(leading: 0.65em, first-line-indent: 12pt, justify: true)

// text characteristics
set text(
  font: "Fira Sans", // New Computer Modern, 
  top-edge: "cap-height",
  bottom-edge: "baseline",
  number-type: "old-style",
)

// math font
show math.equation: set text(font: "Fira Math")

show: chic.with(
  chic-footer(
    center-side: chic-page-number()
  ),
  chic-header(
    left-side: context(document.title),
    right-side: context(document.author.first()),
  ),
  chic-separator(1pt),
  chic-offset(7pt),
  chic-height(1.5cm)
)
body
}
