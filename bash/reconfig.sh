#!/bin/bash

# Path to the .env file
ENV_FILE=".env"

# Check if the .env file exists
if [ ! -f "$ENV_FILE" ]; then
    echo "The .env file was not found."
    exit 1
fi

# Function to read a variable from the .env file
get_env_variable() {
    local var_name=$1
    local value=$(grep -oP "^${var_name}=\K.*" "$ENV_FILE")
    echo "$value"
}

# Function to update a variable in the .env file, handling special characters
update_env_variable() {
    local var_name=$1
    local new_value=$2
    # Escape special characters that might cause issues in sed (/, &, etc.)
    escaped_value=$(echo "$new_value" | sed 's/[&/\]/\\&/g')
    sed -i "s|^${var_name}=.*|${var_name}=${escaped_value}|" "$ENV_FILE"
}

# Function to validate URLs
validate_url() {
    if [[ $1 =~ ^https?://.* ]]; then
        return 0
    else
        return 1
    fi
}

# Function to validate the wallet address format (simple length validation)
validate_wallet_address() {
    if [[ ${#1} -ge 30 ]]; then
        return 0
    else
        return 1
    fi
}

# Function to display and prompt for a variable
handle_variable() {
    local var_name=$1
    local validation_function=$2
    local current_value=$(get_env_variable "$var_name")

    if [ -z "$current_value" ]; then
        echo "$var_name does not have any assigned value."
    else
        echo "Current value of $var_name: $current_value"
    fi

    read -p "Do you want to modify $var_name? (y/n): " modify
    if [[ "$modify" =~ ^[yY]$ ]]; then
        local new_value=""
        while true; do
            read -p "Enter the new value for $var_name: " new_value
            if $validation_function "$new_value"; then
                update_env_variable "$var_name" "$new_value"
                echo "$var_name successfully updated."
                break
            else
                echo "Invalid value. Please try again."
            fi
        done
    fi
}

# Manage the variables
handle_variable "ERGO_NODE_URL" validate_url
handle_variable "ERGO_WALLET_MNEMONIC" validate_wallet_address
handle_variable "ERGO_PAYMENTS_RECIVER_WALLET" validate_wallet_address

echo "Process completed."
