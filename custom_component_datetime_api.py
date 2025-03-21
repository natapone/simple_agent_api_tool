from langflow.custom import Component
from langflow.io import MessageTextInput, Output
from langflow.schema import Data, Message, DataFrame


class DateTimeAPICore(Component):
    display_name = "DateTime API"
    description = "Get current datetime and week number with timezone support."
    icon = "datetime"
    name = "DateTimeAPI"

    # Make API URL configurable
    API_URL = "http://host.docker.internal:8005"  # Changed from 0.0.0.0 to localhost

    inputs = [
        MessageTextInput(
            name="timezone",
            display_name="Timezone",
            tool_mode=True,
            value="UTC",
            placeholder="Enter timezone (e.g., UTC, America/New_York)",
        ),
    ]

    outputs = [
        Output(
            display_name="DateTime",
            name="datetime",
            method="get_datetime",
        ),
        Output(
            display_name="Week Number",
            name="week_number",
            method="get_week_number",
        ),
        Output(
            display_name="DataFrame",
            name="dataframe",
            method="as_dataframe",
        ),
    ]

    def _make_request(self, endpoint: str, params: dict) -> dict:
        """Make HTTP request to API with error handling."""
        try:
            import httpx
            # Use UTC if timezone is empty
            if "timezone" in params and not params["timezone"]:
                params["timezone"] = "UTC"
                
            with httpx.Client(timeout=5.0) as client:  # Add timeout
                response = client.get(
                    f"{self.API_URL}/api/v1/{endpoint}",
                    params=params
                )
                response.raise_for_status()
                return response.json()
        except httpx.ConnectError:
            return {"error": f"Could not connect to API at {self.API_URL}. Make sure the API server is running."}
        except httpx.TimeoutException:
            return {"error": "Request timed out. The API server might be slow or unresponsive."}
        except httpx.HTTPError as e:
            return {"error": f"HTTP error occurred: {str(e)}"}
        except Exception as e:
            return {"error": f"An unexpected error occurred: {str(e)}"}

    def get_datetime(self) -> list[Data]:
        """Get current datetime in ISO format."""
        data = self._make_request("datetime", {"timezone": self.timezone})
        if "error" in data:
            return [Data(text=f"Error: {data['error']}")]
        return [Data(text=data["datetime"])]

    def get_week_number(self) -> Message:
        """Get current week number."""
        data = self._make_request("week-number", {"timezone": self.timezone})
        if "error" in data:
            return Message(text=f"Error: {data['error']}")
        return Message(text=str(data["week_number"]))

    def as_dataframe(self) -> DataFrame:
        """Get all data as a DataFrame."""
        datetime_data = self._make_request("datetime", {"timezone": self.timezone})
        week_data = self._make_request("week-number", {"timezone": self.timezone})
        
        if "error" in datetime_data or "error" in week_data:
            error_msg = datetime_data.get("error", "") or week_data.get("error", "")
            return DataFrame([{"error": error_msg}])
            
        return DataFrame([{
            "datetime": datetime_data["datetime"],
            "week_number": week_data["week_number"],
            "timezone": self.timezone or "UTC"  # Use UTC if timezone is empty
        }]) 