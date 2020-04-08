<template>
<div>

<h1>Create Your Own Room</h1>


        <div class="block">
            <b-radio v-model="labelPosition"
                native-value="Public">
                Public
            </b-radio>
            <b-radio v-model="labelPosition"
                native-value="Private">
                Private
            </b-radio>
        </div>

        <b-field horizontal label="Name of Room" >
            <b-input placeholder="Please enter a name with more than 5 characters"></b-input>
        </b-field>


        <b-field horizontal label="Number of Listeners">
        <b-numberinput :editable="false" min="0" max="15" controls-position="compact"
                controls-rounded></b-numberinput>
        </b-field>

        <b-field horizontal label="Music Genre">
            <b-select placeholder="Select a subject">
                <option value="1">Pop</option>
                <option value="2">Hip-Hop</option>
                <option value="3">Country</option>
                <option value="4">Rock</option>
                <option value="5">R&B</option>
                <option value="6">EDM</option>
                <option value="7">Classical</option>
                <option value="8">Jazz</option>
                <option value="9">Christian</option>
                <option value="10">K-Pop</option>
            </b-select>
        </b-field>

        <b-button type="is-primary" class="createButton">Create Room</b-button>

</div>
    
</template>

<script>
export default {
    name:"newroom",

     data() {
        return {
            labelPosition: 'Public'
        }
    }
}
</script>



<style>
h1{
    font-size: 3em;
}

.block{
    font-size:20px;
}

.label{
    color: white;
    font-size: 2em;
}

.createButton{
    font-size: 2em;
}

.b-radio.radio input[type=radio]:checked + .check {
    border-color: orange;
    background-color: orange;
}

.field-label .label {
    font-size: 18px;
}

</style>