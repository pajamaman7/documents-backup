#import "preamble.typ": preamble
#show: preamble

#import "@preview/fletcher:0.5.8" as fletcher: diagram, node, edge

#set document(
  title: [Assignment $N$],
  author: "Thomas Boyko",
  keywords: "",
  date: auto,
)
//*********************//
// Content Begins Here //
//*********************//

    In the surface $M_g$ of genus $g$, let $C$ be a circle that separates $G_g$ into two compact subsurfaces $M'_h$ and $M_k'$ obtained from the closed surfaces $M_h$ and $M_k$ by deleting an open disk from each. Show that $M'_h$ does not retract onto its boundary circle $C$ and hence $M_g$ does not retract onto $C$. [Hint: abelianize $pi_1$.] But show that $M_g$ does retract onto the nonseparating circle $C'$ in the figure (Hatcher).

Begin with a quick computation of the fundamental group of the punctured surface of genus $g$, $M_g$. Recall the construction of $M_g$ consisted of a single $0$-cell, $2g$ $1$-cells, and a single $2$-cell. Puncturing the $2$-cell with a hole or by removing a single point allows us to retract the hole onto the boundary of the cell. After gluing the boundary to the 1-cells, we will just be left with the $1$-cells, and we will have a homotopy equivalent space, //$bigvee^{2g}S^{1}$. And since we know the fundamental group of the wedge sum, we are left with:
$
    pi_1(S^1)=
$
Now suppose for the sake of contradiction that $M_h'$ did retract onto the boundary circle $C  S^{1}$. Then the inclusion $iota_*: pi_1(S_1) arrow pi_1(M_h')$ would be injective. 

In addition, we have a quotient map $q:pi_1(M_h') arrow ( pi_1(M_h') ) ^{a b}$

$ #diagram(cell-size: 15mm, $
  pi_1(S_1) edge(iota_*, ->>) edge("dr", iota_*q, -->) & pi_1(M_h') edge("d",q,->)\
  &(pi_1(M_h'))^(a b)
$) $


//#exercise[sjkflhajkl]
