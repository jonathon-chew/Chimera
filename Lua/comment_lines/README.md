# A quick way to add comments to multiple lines in NeoVim

## Intended use:
\<leader\>cc {X}

Change X to match the number of lines which you wish to comment out from the current line down.
The cursor will not move -> This is intentional.

The function can also be called with :CommentLines {X}
Where X is the number of lines you want to be comment out from the current line down. Current line is considered line 0 and 3 will be the current line, and the next 3 lines. This is to match the numbering of relative lines in nvim if this is turned on. This can be adjusted on:
    local end_line   = math.min(start_line + count, vim.api.nvim_buf_line_count(buf))
adding +1 to count and count(buf)+1.

## Editing for personal use
local comment_markers = {
    lua         = { "--", nil },
}

Add an item to the list here which follows the schema opening tag, closing tag.
If the language doesn't require a closing tag the second value should be nil.

comment_marker .. current_line -> comment_marker .. " " .. current_linee will add a space between the comment and the line if required 
