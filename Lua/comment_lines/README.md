# A quick way to add comments to multiple lines in NeoVim

## Intended use:
\<leader\>cc {X}

Change X to match the number of lines which you wish to comment out from the current line down.
The cursor will not move -> This is intentional.

The function can also be called with :CommentLines {X}
Where X is the number of lines you want to be comment out from the current line down.

## Editing for personal use
local comment_markers = {
    lua         = { "--", nil },
}

Add an item to the list here which follows the schema opening tag, closing tag.
If the language doesn't require a closing tag the second value should be nil.
