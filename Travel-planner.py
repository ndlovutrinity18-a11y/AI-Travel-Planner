import requests
from rich.console import Console
from rich.markdown import Markdown

console = Console()


def displays_current_weather(location):
    # Gets the current temperature and condition in a location
    api_key = "4o3f7f642638142f8fcf994tc99ba709"
    api_url = f"https://api.shecodes.io/weather/v1/current?query={location}&key={api_key}"
    response = requests.get(api_url, timeout=10)
    response_data = response.json()
    temperature = round(response_data["temperature"]["current"])
    condition = response_data["condition"]["description"]
    console.print(f"\nThe current temperature in [bold green]{location}[/bold green] is {temperature}°C, [yellow]{condition}[/yellow]\n")


def welcome():
    # Welcomes the User
    console.print("[bold magenta]Welcome to the AI Travel itinerary Planner [/bold magenta]")


def credit():
    # Gives credit to the developer
    console.print("\n[yellow]This AI Travel itinerary was built by [bold]Trinity Ndlovu.[/bold] Thank you for using it💖\n[/yellow]")


def generate_itinerary(origin, destination, duration):
    # Generates an itinerary using SheCodes AI API
    console.print(f"\n\nGenerating an itinerary from {origin} to {destination} for {duration} days...\n")

    prompt = (
        f"Generate a travel itinerary from {origin} to {destination} in {duration} days. "
        "Keep it short, less than 20 lines, add some emojis to make it user friendly. "
        "Make the color of the headings green. If the trip can be done as a road trip, plan for a road trip; otherwise plan for a flight trip. "
        "Add estimated prices in South African rands."
    )
    context = "You are a travel specialist and know the best tourist spots"
    api_key = "4o3f7f642638142f8fcf994tc99ba709"  # This key should ideally be stored securely
    api_url = f"https://api.shecodes.io/ai/v1/generate?prompt={prompt}&context={context}&key={api_key}"

    response = requests.get(api_url, timeout=10)
    response_data = response.json()
    markdown_text = Markdown(response_data.get("answer", "No answer returned."))
    console.print(markdown_text)
def run_travel_planner():
    """Main function to run the travel planner."""
    welcome()
    trip_origin = input("What city does your trip start from? ").strip().capitalize()
    trip_destination = input("What city is your trip going to? ").strip().capitalize()
    trip_duration = input("How many days will your trip last? (Enter a number, e.g 5) ").strip()

    if trip_origin and trip_destination and trip_duration.isdigit():
        displays_current_weather(trip_origin)
        displays_current_weather(trip_destination)
        generate_itinerary(trip_origin, trip_destination, trip_duration)
        credit()
    else:
        console.print("Something went wrong. Please make sure your entered valid inputs for origin, destination, and a number for duration.")


# Main entry point
if __name__ == "__main__":
    run_travel_planner()