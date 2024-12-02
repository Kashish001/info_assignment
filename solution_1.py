#!/usr/bin/python3

from typing import Self, Optional

class DataStream:
    """
    A class that manages a stream of data strings, ensuring that each unique
    string is output at most once every 5 seconds.
    """
    def __init__(self: Self) -> None:
        """
        Initializes the DataStream object and declared the storage for
        tracking last data_stream chunk.
        """
        self.last_data_stream_chunk: Optional[dict[str, int]] = None

    def should_output_data_str(self: Self, timestamp: int, data_string: str) -> bool:
        """ Check whether data_stream could be outputted based on timestamp
         differences which should be at most 5 seconds.

        Args:
            timestamp: Timestamp of current data_string.
            data_string: The data string that needs to be processed now.

        Returns:
            bool: If data string could be outputted True otherwise False.
        """

        # Check if there is any chunk before this
        if not self.last_data_stream_chunk:
            self.last_data_stream_chunk = {data_string: timestamp}
            return True

        # Check if that data_str is already present or not
        if data_string in self.last_data_stream_chunk:
            chunks_time_diff: int = abs(self.last_data_stream_chunk[data_string] - timestamp)
            # check if time diff is at most 5
            if chunks_time_diff >= 5:
                # Update timestamp of data_str
                self.last_data_stream_chunk[data_string] = timestamp
                return True
            return False
        # If it's a new data string that hasn't been seen before, add it to the dictionary
        self.last_data_stream_chunk[data_string] = timestamp
        return True


data_stream = DataStream()
print(data_stream.should_output_data_str(timestamp=0, data_string="hello"))
print(data_stream.should_output_data_str(timestamp=1, data_string="world"))
print(data_stream.should_output_data_str(timestamp=6, data_string="hello"))
print(data_stream.should_output_data_str(timestamp=7, data_string="hello"))
print(data_stream.should_output_data_str(timestamp=8, data_string="world"))
