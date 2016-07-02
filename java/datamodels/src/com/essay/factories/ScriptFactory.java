package com.essay.factories;

import java.util.List;

import com.essay.models.Block;
import com.essay.models.Desire;
import com.essay.models.Goal;
import com.essay.models.GoalOperator;
import com.essay.models.GoalPriority;
import com.essay.models.GoalSection;
import com.essay.models.ObjValue;
import com.essay.models.Script;
import com.essay.models.SectionType;

public interface ScriptFactory {
	public Script createScript(List<Block> blockList);
	public Block createBlock(List<Desire> desireList);
	public Desire createDesire(List<GoalSection> sectionList);
	public GoalSection createGoalSection(SectionType type,GoalPriority priority,List<Goal> goalList);
	public Goal createGoal(String subject, String predicate, String alias,GoalOperator operator,ObjValue value);

}
