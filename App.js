import React, { useState } from "react";
import { StatusBar } from "expo-status-bar";
import {
  StyleSheet,
  Text,
  TextInput,
  ScrollView,
  TouchableOpacity, // Import TouchableOpacity for the button
} from "react-native";
import { Picker } from "@react-native-picker/picker";

export default function App() {
  const [nameSurname, setNameSurname] = useState("");
  const [birthDate, setBirthDate] = useState("");
  const [educationLevel, setEducationLevel] = useState("");
  const [city, setCity] = useState("");
  const [gender, setGender] = useState("");
  const [aiModel, setAiModel] = useState([]);
  const [defectsCons, setDefectsCons] = useState("");
  const [useCase, setUseCase] = useState("");

  const handleSelectAiModel = (model) => {
    if (aiModel.includes(model)) {
      setAiModel(aiModel.filter((m) => m !== model));
    } else {
      setAiModel([...aiModel, model]);
    }
  };

  const allFieldsFilled =
    nameSurname &&
    birthDate &&
    educationLevel &&
    city &&
    gender &&
    aiModel.length > 0 &&
    defectsCons &&
    useCase;

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text>Welcome to our mobile AI survey!</Text>
      <TextInput
        placeholder="Name-surname"
        style={styles.input}
        onChangeText={(text) =>
          /^[A-Za-z ]+$/.test(text) || text === "" ? setNameSurname(text) : null
        }
        value={nameSurname}
      />
      <TextInput
        placeholder="Birth Year (YYYY)"
        style={styles.input}
        onChangeText={(text) =>
          /^\d{0,4}$/.test(text) ? setBirthDate(text) : null
        }
        value={birthDate}
      />

      <TextInput
        placeholder="Education Level"
        style={styles.input}
        onChangeText={(text) =>
          /^[A-Za-z ]+$/.test(text) || text === ""
            ? setEducationLevel(text)
            : null
        }
        value={educationLevel}
      />
      <TextInput
        placeholder="City"
        style={styles.input}
        onChangeText={(text) =>
          /^[A-Za-z ]+$/.test(text) || text === "" ? setCity(text) : null
        }
        value={city}
      />
      <Picker
        selectedValue={gender}
        style={styles.picker}
        onValueChange={(itemValue) => setGender(itemValue)}
      >
        <Picker.Item label="Select Gender" value="" />
        <Picker.Item label="Male" value="male" />
        <Picker.Item label="Female" value="female" />
        <Picker.Item label="Other" value="other" />
      </Picker>
      <Text>AI Models/TYPES you've tried (Select multiple):</Text>
      {["ChatGPT", "Bard", "Claude", "Copilot"].map((model) => (
        <Text
          key={model}
          onPress={() => handleSelectAiModel(model)}
          style={aiModel.includes(model) ? styles.selectedItem : styles.item}
        >
          {model}
        </Text>
      ))}
      <TextInput
        placeholder="Defects or cons of the model(s)"
        style={styles.input}
        multiline
        onChangeText={setDefectsCons}
        value={defectsCons}
      />
      <TextInput
        placeholder="Use case of AI in daily life"
        style={styles.input}
        multiline
        onChangeText={setUseCase}
        value={useCase}
      />
      {allFieldsFilled && (
        <TouchableOpacity style={styles.button}>
          <Text style={styles.buttonText}>Send</Text>
        </TouchableOpacity>
      )}
      <StatusBar style="auto" />
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    height: "100vh",
    alignItems: "center",
    justifyContent: "center",
    paddingTop: 20,
  },
  input: {
    width: "80%",
    padding: 10,
    margin: 10,
    borderWidth: 1,
    borderColor: "gray",
    borderRadius: 5,
  },
  picker: {
    width: "80%",
    margin: 10,
  },
  item: {
    padding: 10,
  },
  selectedItem: {
    padding: 10,
    backgroundColor: "lightgrey",
  },
  button: {
    backgroundColor: "#007AFF",
    padding: 10,
    borderRadius: 5,
    marginTop: 10,
  },
  buttonText: {
    color: "#FFFFFF",
    fontSize: 16,
    textAlign: "center",
  },
});
