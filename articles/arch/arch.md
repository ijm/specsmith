# A taxonomy of technical architecture documents

A lot of technical documentation has always been a form of declarative constraint programming wrapped in the idioms of natural language. While often taught as a form of communication or protocol (ref), the idea of specifications as code has been around a long time and is seen in idioms like test-driven development (ref). However, with a little formalization in the right direction, we can make this coding idea more useful given the shift to using AI tools. There are lots of guides on 'how to write a specification', 'how to write requirements', or style guides, etc. (ref). LLMs don't mind repetition, like structured documents, and don't complain when given a dry book to read.

If we want to treat technical documentation more like code we need to understand what statements in the documentation do or mean. We can split technical documents up into narrative like documents whose goal is to explain, describe, or teach more general concepts, and non-narrative like documents like specifications, requirements, procedures, styles, or rules, which really are a program for a human, and is the group we'll focus on here.

::: {.aside} 
The word program comes from the Late Latin (and Greek) programma, meaning "a written public notice or edict", and was first used in English circa 1630, shifting to a public agenda of activities or events circa 1800, and finally to a definite plan or scheme by the mid-1800s. I don't think we need to reclaim that meaning, but the punchy imperative language favored in specifications or procedures certainly retains the spirit.
:::

Formalization usually involves categorizing, that is, picking boundaries to distinguish between categories in some taxonomy. This is often mistaken as defining objects or categories, but really it's defining the boundaries and the rules that show how something stands in relation to other things that are important. The definitions or categories emerge and come along for the ride. It's how we tell that something is green that defines what green is. This is not a trivial distinction and getting it the wrong way around leads to significant problems.

Formalization then often becomes a seemingly pedantic game of taking some object that we know how to deal with, figuring out the rules that fit that object, and re-defining such objects based on those rules. While we are going to play that game in this article, it's that 'that we know how to deal with' that must be kept in mind: Formal 'well defined' definitions reuse names for object to cover just the part we know how to deal with. Inventing new words, or naming something after someone are also options, but they often lead to impenetrable language.

Later we'll look at how we can plagiarize the idea use of capitalization of words from the legal profession to distinguish between a colloquial and specific use, but first we need the boundaries.

Defining boundaries is exactly what specification like statements do, for example, 'The device MUST have a capacity of at least 300 Whr'; this is a nice clear boundary.

So one of our categories should be defined by these boundary descriptions, common in specifications, requirements, and styles, that define some metric which we can measure or determine.

This metrology view leads to a neat geometric description: Each boundary description defines a space the measurement lives in and a boundary or acceptable range in that space. The composition of these boundaries literally forms a constraint space:  The intersection of the boundaries forms some shape in an odd high dimensional space that is the product of all of the individual spaces. (see insert for detail explanation). A complete set of measurements then forms a vector in this space, and the specification is met if that point falls inside the shape defined.

Building these kinds of high dimensional spaces and shapes is exactly how machine learning and LLMs work, so it is no surprise they work well with clear specifications.

As a last comp-sci-nerd rather than mathematical observation, in this construction each boundary is a 'point' and this declarative language is the logical dual or complement (literally the orthogonal complement if the feasibility space forms linear equations in a vector space) to a tacit program where the points are irrelevant. A good specification then generates a clean separation of something into its tacit and pointed parts.

More generally specifications define the boundary of feasible behavior while tacit programs define paths through that space. An AI code generator then is essentially finding the tacit programs that satisfy the constraint manifolds defined by specifications.

This duality is quite deep, but for this article we don't need to go into more detail.

Next we can also classify boundary statements based on where the constraint comes from:

* is it an external constraint from a customer or stake holder, or something computed internally to meet some other higher constraints.

* The second is more subtle and can be summed up as: is the constraint prescribed or forced for all solutions, or a choice for this solution?
  In computer science or mathematics, we'd call this a 'universal' versus an 'existential' constraint if we push things to there extremes: universal constraints must be met for all solutions (for all solutions X must be true) and define a constraint space; existential constraints are required for a specific solution (there exists a solution for which X is true) and define a point in solution space. In reality this boundary is a little most blurred (e.g. must becomes should). For example specifying a 1 amp hr battery to meet some other requirement is a forced universal specification, while choosing the battery to be pink is a existential condition for a solution need to actually buy the battery.

Now we can use these axes to bin and name documents: specification documents are universal-internal, requirements documents are universal-external, style documents are existential-internal, and rule documents are existential-external.

However this is just a choice of axes. We could instead base the taxonomy on who has authority to change a constraint, so who do you have to call or who would you put on a change control board. Specifications are usually project or group level controlled by a project manager, while requirements involve customers or stakeholders, styles are organization-wide, and rules are there to avoid talking to or because you can't talk to an authority.

Similarly we could replace the internal/external axis with the idea of common knowledge: styles and rules are forms of common knowledge that keep everyone on the same page, that is, everyone agrees on them and importantly knows everyone else agrees on them too; while specifications and requirements are local and require personnel to be 'read-in' to the project.

This distinction is useful because it manifests a tech debt that is often ignored. The project guru problem, where a single person has knowledge that never seems to get documented, is well known, but the same happens with common knowledge, that is, everyone knows or agrees on something that never gets written down. Newbies are newbies precisely because they don't yet know this 'common' knowledge. While this manifests in a human environment as quick embarrassing but amusing conversations with older colleagues, it hamstrings AIs that have no way of learning by their mistakes and instead require such things to be explicitly added to their prompts. These additions are usually ad-hoc and psychologically treated as unimportant or obvious exactly because the knowledge is common. This is has been referred to as the institutional wisdom problem (ref).

Perhaps interestingly, this taxonomic framework itself represents a 'style' choice; an internal, existential decision about how to organize constraint types. This is important because it highlights that there isn't 'one true way' to write technical documents, and that the boundaries are blurred not just because they're on a grey-scale but because the axes can be completely different, while resulting in roughly the same named categories.  A good technical writer, like a good programmer, should be able to switch between these styles and use the local style currently in use, while also being able to argue or justify why a particular style is better suited to a particular job.

The legal profession has long used the idiom of CAPITALIZATION to highlight when to pay attention to this style shift (ref), where there is a precise local definition of the term. Specifications like RFC2119 use this to define words like MUST, and SHOULD, and state that the lower case versions of words should be read as colloquial or common usage.

We can define 'Definition Statements' then as a named boundary statement, where we capitalize the names. For example:
 "GREENS have an HSV hue of 110 \pm 30 degrees, or a wavelength of 530 \pm 35 nm."

