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

function Pandoc(el)
    local latex_defs = {}
    
    local meta_vars = {"githash", "docname", "copyright", "license", "audience", "scope", "revision", "hash"}
    
    table.insert(el.blocks, 1, pandoc.RawBlock("latex",
      "\\vspace{0cm}\\boilerplate\\vspace{1cm}"))
    for _, varname in ipairs(meta_vars) do
        local value = el.meta[varname]
        if value then
            local str_value = pandoc.utils.stringify(value)
            if str_value ~= "" then
                local def = string.format("\\def\\the%s{%s}", varname, str_value)
                table.insert(el.blocks, 1, pandoc.RawBlock("latex", def))
            end
        end
    end
    
    return el
end