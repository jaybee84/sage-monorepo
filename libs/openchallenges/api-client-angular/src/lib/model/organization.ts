/**
 * OpenChallenges API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


/**
 * An organization
 */
export interface Organization { 
    /**
     * An email address.
     */
    email?: string;
    /**
     * The login of an organization
     */
    login: string;
    name?: string;
    avatarUrl?: string | null;
    websiteUrl?: string;
    description?: string;
    /**
     * The unique identifier of an organization
     */
    id: number;
    createdAt: string;
    updatedAt: string;
}
