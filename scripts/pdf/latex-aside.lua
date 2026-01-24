function Div(el)
    if el.classes[1] == "aside" then
      -- insert element in front
      table.insert(
        el.content, 1,
        pandoc.RawBlock("latex", "\\begin{aside}"))
      -- insert element at the back
      table.insert(
        el.content,
        pandoc.RawBlock("latex", "\\end{aside}"))
    end
    return el
end