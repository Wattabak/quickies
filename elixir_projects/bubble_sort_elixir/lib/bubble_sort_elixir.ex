defmodule BubbleSort do
  @moduledoc """
  Documentation for `BubbleSort`.
  """

  @doc """

  """
  @spec sort(List.t()) :: List.t()
  def sort(list) do
    n = Kernel.length(list)

    Enum.each(1..n, fn i ->
      if list[i - 1] > list[i] do
      end
    end)

    unless n >= 1 do
      sort(list)
    end
  end
end
