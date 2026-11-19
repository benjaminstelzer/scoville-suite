# Interface wording

## UI wording and terminology

These rules cover new and changed interface text and need no dictionary,
glossary or terminology record.

For a correction to existing text, preserve its translation, formatting and
escaping behavior, and keep the visible label in the accessible name.

Use approved product and platform terms. Where none exists, choose the word
this audience and domain normally use, following established conventions.

Follow an explicit language request first, then the language of the product
or its source and the platform's conventions. The chat language alone does not
override them. For new UI with none of these, state the chosen language
briefly. Ask only when the choice materially affects the product outcome.

- One term per concept within each language, in every affected view and
  state: not `Workspace` in the list and `Project` in its dialog for the
  same thing. Grammatical forms and context-dependent short forms may vary;
  different things keep different words.
- A heading names its topic, a button its action or effect, a field its
  value, a toggle its property. Add the object, unit or consequence a label
  needs: `Timeout (seconds)`.
- Text is written from the user's position: what they see, what they can do
  next and what happens then. It names no file, setting key, internal limit
  or phase of the implementation unless the user has to act on exactly that.
- A text claims only what the code behind it does in that state: a count
  covers what its label names, a word for a result excludes what failed,
  and a next step points to an action the product offers and that is
  present and enabled there.
- A control's visible text stays in its accessible name, and a text is not
  shortened, split or invented to hide a layout problem.
- A translation keeps meaning, conceptual distinctions and established
  technical terms. Follow the target language's conventions and approved
  terms; do not translate technical terms word by word.
