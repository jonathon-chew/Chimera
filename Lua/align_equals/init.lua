local M = {}

-- Function to align equals signs
-- mode not used - as not looking for visual or normal mode atm
function M.align_equals(mode, lines_below)
  local bufnr         = vim.api.nvim_get_current_buf()
  local start_row, end_row

  -- Normal mode: get current line and calculate range
  local current_line  = vim.fn.line('.')
  start_row           = current_line - 1
  end_row             = start_row + (lines_below or 0)

  -- Get lines in the range
  local lines     = vim.api.nvim_buf_get_lines(bufnr, start_row, end_row + 1, false)

  -- Find the max column of '='
  local max_col   = 0
  for _, line in ipairs(lines) do
    local eq_pos  = line:find('=')
    if eq_pos and eq_pos > max_col then
      max_col     = eq_pos
    end
  end

  -- Adjust each line to align '='
  local adjusted_lines  = {}
  for _, line in ipairs(lines) do
    local eq_pos = line:find('=')
      if eq_pos then
        local before_eq = line:sub(1, eq_pos - 1)
        local after_eq  = line:sub(eq_pos)
        local padding   = string.rep(' ', max_col - eq_pos)
        table.insert(adjusted_lines, before_eq .. padding .. after_eq)
      else
        table.insert(adjusted_lines, line) -- No '=' in this line, leave unchanged
      end
  end

  -- Replace lines in buffer
  -- print(' ', bufnr, start_row, end_row, adjusted_lines)
  print(" Start row: ", start_row, "end row: ", end_row)
  vim.api.nvim_buf_set_lines(bufnr, start_row, end_row + 1, false, adjusted_lines)
end

-- Command to align with prompt for lines below
function M.prompt_align()
  local lines_below = tonumber(vim.fn.input('Align equals over how many lines below? '))
  if lines_below then
    M.align_equals('normal', lines_below)
  end
end

-- Setup key mappings or commands
--function M.setup()
--  -- Normal mode command
--  vim.api.nvim_set_keymap('n', '<leader>ae', "<cmd>lua require'align_equals'.prompt_align()<CR>",
--    { noremap = true, silent = true })
--end

return M
