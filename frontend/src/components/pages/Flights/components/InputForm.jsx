import FormInput from "components/atoms/input/Input";
import Button from "components/atoms/button/Button";

export const InputForm = ({ handleSearch, searchQuery, setSearchQuery }) => {
  return (
    <form onSubmit={handleSearch}>
      <label>
        {" "}
        Airport IATA:
        <FormInput
          type="text"
          placeholder={"Search for an Airport"}
          name="airport"
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
        />
      </label>
      <Button title="Find Departures" color="primary" type="submit" />
    </form>
  );
};
