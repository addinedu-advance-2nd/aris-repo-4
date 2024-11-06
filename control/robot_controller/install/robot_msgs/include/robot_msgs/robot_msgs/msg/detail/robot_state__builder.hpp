// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from robot_msgs:msg/RobotState.idl
// generated code does not contain a copyright notice

#ifndef ROBOT_MSGS__MSG__DETAIL__ROBOT_STATE__BUILDER_HPP_
#define ROBOT_MSGS__MSG__DETAIL__ROBOT_STATE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "robot_msgs/msg/detail/robot_state__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace robot_msgs
{

namespace msg
{

namespace builder
{

class Init_RobotState_temperatures
{
public:
  explicit Init_RobotState_temperatures(::robot_msgs::msg::RobotState & msg)
  : msg_(msg)
  {}
  ::robot_msgs::msg::RobotState temperatures(::robot_msgs::msg::RobotState::_temperatures_type arg)
  {
    msg_.temperatures = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_msgs::msg::RobotState msg_;
};

class Init_RobotState_positions
{
public:
  explicit Init_RobotState_positions(::robot_msgs::msg::RobotState & msg)
  : msg_(msg)
  {}
  Init_RobotState_temperatures positions(::robot_msgs::msg::RobotState::_positions_type arg)
  {
    msg_.positions = std::move(arg);
    return Init_RobotState_temperatures(msg_);
  }

private:
  ::robot_msgs::msg::RobotState msg_;
};

class Init_RobotState_position_code
{
public:
  explicit Init_RobotState_position_code(::robot_msgs::msg::RobotState & msg)
  : msg_(msg)
  {}
  Init_RobotState_positions position_code(::robot_msgs::msg::RobotState::_position_code_type arg)
  {
    msg_.position_code = std::move(arg);
    return Init_RobotState_positions(msg_);
  }

private:
  ::robot_msgs::msg::RobotState msg_;
};

class Init_RobotState_angles
{
public:
  Init_RobotState_angles()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RobotState_position_code angles(::robot_msgs::msg::RobotState::_angles_type arg)
  {
    msg_.angles = std::move(arg);
    return Init_RobotState_position_code(msg_);
  }

private:
  ::robot_msgs::msg::RobotState msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_msgs::msg::RobotState>()
{
  return robot_msgs::msg::builder::Init_RobotState_angles();
}

}  // namespace robot_msgs

#endif  // ROBOT_MSGS__MSG__DETAIL__ROBOT_STATE__BUILDER_HPP_
