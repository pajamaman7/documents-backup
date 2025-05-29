Given an alphabet $\Sigma$, we define a [[Formal Language|Regular Language]] over $\Sigma$ recursively:
- The expression $\varnothing$ corresponds to $L(\varnothing)=\varnothing$
- $a$ corresponds to $L(a)=\{ a \}$
- $r_{1}+r_{2}$ corresponds to $L(r_{1})\cup L(r+2)$
- $r_{1}r_{2}$ corresponds to $L(r_{1})L(r_{2})$
- $r_{1}^+$ corresponds to $L(r_{1})^{+}$
- $r_{1}^*$ corresponds to $L(r_{1})^{*}$
Each regular expression defines a [[Formal Language|Regular Language]].