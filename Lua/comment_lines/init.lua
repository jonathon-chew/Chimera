-- It's lua, it needs this?!
local M = {}

-- Table of comment markers for different filetypes
local comment_markers = {
    lua         = { "--", nil },
    python      = { "#", nil },
    javascript  = { "//", nil },
    java        = { "//", nil },
    c           = { "//", nil },
    cpp         = { "//", nil },
    html        = { "<!--", "-->" },
    css         = { "/*", "*/" },
    markdown    = { "<!--", "-->" },
    sh          = { "#", nil },
    go          = { "//", nil},
}

-- Adds comment markers to the start of lines based on filetype
function M.comment_lines(count)
    -- Get the current buffer and cursor position
    local buf        = vim.api.nvim_get_current_buf()
    local cursor     = vim.api.nvim_win_get_cursor(0)
    local start_line = cursor[1] - 1 -- Lua uses 0-based indexing for lines

    -- Get the filetype of the current buffer
    local filetype   = vim.bo.filetype
    local markers    = comment_markers[filetype] or { "#", nil }
    local comment_marker, close_marker = markers[1], markers[2]

    -- Calculate the end line based on the count
    local end_line   = math.min(start_line + count, vim.api.nvim_buf_line_count(buf))

    -- Loop through the lines and prepend the comment marker
    for line = start_line, end_line do
        local current_line = vim.api.nvim_buf_get_lines(buf, line, line + 1, false)[1]
        if line == end_line and close_marker then
            -- Add both the opening and closing marker to the last line
            vim.api.nvim_buf_set_lines(buf, line, line + 1, false, { comment_marker .. current_line .. " " .. close_marker })
        else
            -- Add only the opening marker to other lines
            vim.api.nvim_buf_set_lines(buf, line, line + 1, false, { comment_marker .. current_line })
        end
    end
end

---- Create a command that calls the function
vim.api.nvim_create_user_command(
    "CommentLines",
    function(opts)
        M.comment_lines(tonumber(opts.args))
        end,
        { nargs = 1 } -- Requires exactly one argument (number of lines)
    )

return M
